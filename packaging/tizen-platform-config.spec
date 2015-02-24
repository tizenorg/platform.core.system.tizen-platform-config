%define libname libtzplatform-config
%define keepstatic 1

Name:           tizen-platform-config
Version:        2.0
Release:        0
Summary:        Tizen Platform Configuration
License:        MIT
Url:            http://www.tizen.org
Group:          System/Configuration
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source1001:     %{name}.manifest
BuildRequires:  tizen-platform-wrapper >= 2

# the main package only contains a config file but other dependent packages
# will contain binary. So, we can't build a noarch package and have to avoid
# a rpmlint warning using a filter in xxx-rpmlintrc

%description
Tizen Platform Configuration - variables definitions

%package -n %{libname}
Summary:        Tizen Platform Configuration - helper library
Group:          System/Libraries
License:        LGPL-2.0
Requires:       %{name} = %{version}
Requires:       %{name}-skel = %{version}
%description -n %{libname}
Tizen Platform Configuration - helper library to lookup Tizen variables easily

%package -n %{libname}-devel
Summary:        Tizen Platform Configuration - helper libray headers, RPM macros
Group:          Development/Libraries
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{libname}-devel
Tizen Platform Configuration - helper library headers to include in source code,
RPM macros to call in spec files

%package -n %{name}-tools
Summary:        Tizen Platform Configuration - tools
Group:          System/Utilities
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{name}-tools
Tizen Platform Configuration - helper program to lookup Tizen variables easily

%package skel
Summary:        Tizen Platform Configuration - skeleton directory
Group:          System/Configuration
License:        LGPL-2.0
%description skel
Tizen Platform Configuration - skeleton directory for supporting the default
tizen user directory hierarchy

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --enable-static
%__make %{?_smp_mflags}

%check
%__make check

%install
%make_install

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license MIT
%config %{_sysconfdir}/tizen-platform.conf

%files -n %{libname}
%manifest %{name}.manifest
%{_libdir}/*.so.*

%files -n %{libname}-devel
%manifest %{name}.manifest
%license LGPL_2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%config %{_sysconfdir}/rpm/macros.tizen-platform
%{_libdir}/*.a

%files -n %{name}-tools
%manifest %{name}.manifest
%{_bindir}/*

%files skel
%manifest %{name}.manifest
%{_sysconfdir}/skel/
