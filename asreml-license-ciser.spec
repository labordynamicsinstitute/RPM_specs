Name: asreml-license-ciser
License: Commercial
Group: Application/Statistics
Summary: ASReml license from vsn-int.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.10
Release: 1 
Requires: asreml >= 1.10
#Source0: ASReml.ciser.alx
Source0: vrdc6401.ali
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 ASReml license for CISER (site license).
%prep

%build

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/usr/local/etc/asreml
export ASREML_LICENSE_FILE=%buildroot/usr/local/etc/asreml/ASReml.alx
ASREML110 -n %{SOURCE0}

%clean

%files
/usr/local/etc/asreml/ASReml.alx

%changelog
* Wed May 24 2006 lars.vilhuber@cornell.edu
- made the license rpm work with the .ali file
* Wed Jan 6 2006 lars.vilhuber@cornell.edu
- License for CISER
