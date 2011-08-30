Name: asreml3-license-vrdc
License: Commercial
Group: Application/Statistics
Summary: ASReml license from vsn-int.com for VRDC
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 3
Release: 1 
Requires: asreml3 >= 3
Source0: asreml.lic
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
This is the ASReml license for VRDC (network license).
%prep

%build

%install
cd %buildroot
install -d %buildroot/opt/asreml3/bin
install  %{SOURCE0} %buildroot/opt/asreml3/bin

%post

%clean

%files
/opt/asreml3/bin/asreml.lic

%changelog
* Mon Aug 29 2011 lars.vilhuber@cornell.edu
  - Modification for ASReml3
