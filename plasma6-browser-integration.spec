%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-browser-integration
Version: 6.1.3
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-browser-integration/-/archive/%{gitbranch}/plasma-browser-integration-%{gitbranchd}.tar.bz2#/plasma-browser-integration-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-browser-integration-%{version}.tar.xz
%endif
Summary: Better browser integration for the Plasma desktop
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(LibTaskManager) >= 5.27.80

%description
Better browser integration for the Plasma desktop.

%prep
%autosetup -p1 -n plasma-browser-integration-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DINSTALL_CHROME_MANIFEST=TRUE -DMOZILLA_DIR:PATH=%{_libdir}/mozilla \
	-G Ninja

%build
%ninja_build -C build

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
%{_qtdir}/plugins/kf6/kded/browserintegrationreminder.so
%{_datadir}/chromium/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/google-chrome/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/applications/org.kde.plasma.browser_integration.host.desktop
