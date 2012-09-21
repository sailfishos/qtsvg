%define _qtmodule_snapshot_version 5.0.0-beta1
Name:       qt5-qtsvg
Summary:    Qt scripting module
Version:    5.0.0~beta1
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
#Source0:    %{name}-%{version}.tar.xz
Source0:    qtsvg-opensource-src-%{_qtmodule_snapshot_version}.tar.xz
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
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module development files

%package plugin-imageformat-svg
Summary:    Qt SVG image format plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-imageformat-svg
This package contains the SVG image format plugin

%package plugin-iconengine-svg
Summary:    Qt SVG icon image plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-iconengine-svg
This package contains the SVG icon image plugin



#### Build section

%prep
%setup -q -n qtsvg-opensource-src-%{_qtmodule_snapshot_version}


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.so.5
%{_libdir}/libQtSvg.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.so
%{_libdir}/libQtSvg.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/

%files plugin-imageformat-svg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/lib*svg.so

%files plugin-iconengine-svg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/iconengines/lib*svg*.so

#### No changelog section, separate $pkg.changes contains the history
