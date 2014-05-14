%define libname libtzplatform-config

Name:           tizen-platform-config
Version:        1.0
Release:        0
Summary:        Tizen Platform Configuration 
License:        MIT
Url:            http://www.tizen.org
Group:          System/Configuration
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source1001:     %{name}.manifest
BuildRequires:  tizen-platform-wrapper   

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
%description -n %{libname}
Tizen Platform Configuration - helper library to lookup Tizen variables easily

%package -n %{libname}-devel
Summary:        Tizen Platform Configuration - helper libray headers, RPM macros
Group:          Development/Libraries
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{libname}-devel
Tizen Platform Configuration - helper library headers to include in source code, RPM macros to call in spec files

%package -n %{name}-tools
Summary:        Tizen Platform Configuration - tools
Group:          System/Utilities
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{name}-tools
Tizen Platform Configuration - helper program to lookup Tizen variables easily

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure \
    --disable-static

make %{?_smp_mflags}

%check
make check

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

%files -n %{name}-tools
%manifest %{name}.manifest
%{_bindir}/*
