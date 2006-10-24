Name: asreml-license-nsf01
License: Commercial
Group: Application/Statistics
Summary: ASReml license from vsn-int.com for NSF01 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.10
Release: 1 
Requires: asreml >= 1.10
Source0: nsf01.ali
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 ASReml license for NSF01.
%prep

%build

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/usr/local/etc/asreml
install -m 755 -g root -o root %{SOURCE0} %buildroot/usr/local/etc/asreml/

%post
export ASREML_LICENSE_FILE=/usr/local/etc/asreml/ASReml.alx
[[ -f $ASREML_LICENSE_FILE ]] && mv $ASREML_LICENSE_FILE
cd /usr/local/etc/asreml
/usr/local/bin/ASREML110 -n %{SOURCE0}

%clean

%files
/usr/local/etc/asreml/nsf01.ali

%changelog
* Wed May 24 2006 lars.vilhuber@cornell.edu
- made the license rpm work with the .ali file
* Wed Jan 6 2006 lars.vilhuber@cornell.edu
- License for NSF01
