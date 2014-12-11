%define         _state          stable
%define		orgname		libkface
%define         qtver           4.8.1

Summary:	Library to perform face recognition and detection over pictures
Name:		kde4-libkface
Version:	14.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/applications/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b2b850826cbb18b00deb18568f20c3bb
URL:		http://www.kde.org/
BuildRequires:	opencv-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Qt/C++ wrapper around LibFace library to perform face recognition
and detection over pictures.

%package devel
Summary:	Header files for libkface development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkface
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkface development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkface.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkface.so.3
%attr(755,root,root) %{_libdir}/libkface.so.*.*.*
%{_datadir}/apps/libkface

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkface.so
%{_includedir}/libkface
%{_pkgconfigdir}/libkface.pc
%{_libdir}/cmake/Kface-*
