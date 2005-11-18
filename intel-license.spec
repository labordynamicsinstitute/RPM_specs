Name: intel-license-development
License: Commercial
Group: Development/Languages
Summary: Intel 8 license for development use at CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8 
Release: 0 
Source0: intel-licenses-development.tgz 
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
/opt/intel/licenses/w_mckinley_1901-44665345.lic
/opt/intel/licenses/serialnumbers.development.txt


%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
