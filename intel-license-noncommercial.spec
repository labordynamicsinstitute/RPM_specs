Name: intel-license-noncommercial
License: Commercial
Group: Development/Languages
Summary: Intel 8 license for non-commerical use at CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8 
Release: 0 
Source0: intel-licenses-noncommercial.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch 

%description
This is CISER's Linux Intel compiler license. You will need to install it before using the Intel compilers.

%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/opt/intel/licenses
cd %buildroot/opt/intel/licenses
tar xzf %{SOURCE0}
chmod 0755  %buildroot/opt/intel/licenses/*

%clean

%files
/opt/intel/licenses/noncommercial_cpp_l_N4R8-T767JCSW.lic
/opt/intel/licenses/noncommercial_for_l_N9WP-VSG22VV3.lic
/opt/intel/licenses/noncommercial_mkl_l_N9HJ-XNTBDGX9.lic
/opt/intel/licenses/serial-numbers


%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
