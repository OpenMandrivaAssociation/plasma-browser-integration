%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-browser-integration
Version: 5.26.3
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
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Purpose)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(LibTaskManager)

%description
Better browser integration for the Plasma desktop.

%prep
%autosetup -p1
%cmake_kde5 -DINSTALL_CHROME_MANIFEST=TRUE  -DMOZILLA_DIR:PATH=%{_libdir}/mozilla

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_sysconfdir}/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_datadir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_bindir}/plasma-browser-integration-host
%{_libdir}/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/qt5/plugins/kf5/kded/browserintegrationreminder.so
%{_datadir}/chromium/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/google-chrome/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/applications/org.kde.plasma.browser_integration.host.desktop
