%define _disable_lto 1
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-browser-integration
Version: 5.13.4
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Better browser integration for the Plasma desktop
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)

%description
Better browser integration for the Plasma desktop

%prep
%autosetup
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_bindir}/plasma-browser-integration-host
%{_prefix}/lib/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/qt5/plugins/kf5/kded/browserintegrationreminder.so
%{_libdir}/qt5/plugins/krunner_browsertabs.so
%{_datadir}/kservices5/plasma-runner-browsertabs.desktop