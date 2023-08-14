Name:       qt5-qtsvg
Summary:    Qt SVG module
Version:    5.6.2
Release:    1
License:    (LGPLv2 or LGPLv3) with exception or GPLv3 or Qt Commercial
URL:        http://www.qt.io
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module


%package devel
Summary:    Qt SVG - development files
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module development files

%package plugin-imageformat-svg
Summary:    Qt SVG image format plugin
Requires:   %{name} = %{version}-%{release}

%description plugin-imageformat-svg
This package contains the SVG image format plugin

%prep
%setup -q -n %{name}-%{version}

%build
touch .git
%qmake5 QT.widgets.name= DEFINES+=QT_NO_WIDGETS
%make_build

%install
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# these manage to really royally screw up cmake
find %{buildroot}%{_libdir} -type f -name "*_*Plugin.cmake" \
-exec rm {} \;
#
%fdupes %{buildroot}/%{_includedir}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%license LICENSE.LGPLv21
%license LICENSE.LGPLv3
%license LGPL_EXCEPTION.txt

%{_qt5_libdir}/libQt5Svg.so.5
%{_qt5_libdir}/libQt5Svg.so.5.*

%files devel
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Svg.so
%{_qt5_libdir}/libQt5Svg.prl
%{_qt5_libdir}/pkgconfig/*
%{_qt5_includedir}/*
%{_qt5_archdatadir}/mkspecs/
%{_qt5_libdir}/cmake/

%files plugin-imageformat-svg
%defattr(-,root,root,-)
%{_qt5_plugindir}/imageformats/lib*svg.so
%{_qt5_plugindir}/iconengines/libqsvgicon.so

