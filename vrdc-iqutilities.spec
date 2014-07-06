Name: vrdc-iqutilities
License: GPL
Group: Applications/Statistical
Summary: Creates i(PROG) and q(PROG) convenience short cuts to interact with a PBS-like qsub system
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1
Release: 3 
Source0: vrdc-iutilities.tgz
Source1: vrdc-qutilities.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
Creates i(PROG) and q(PROG) convenience short cuts to interact with a PBS-like qsub system

%prep

%build
# create it - optionally comment out
tar czvf %{SOURCE0} /usr/local/bin/i*
tar czvf %{SOURCE1} /usr/local/bin/q*

%install
install -d -m 755 %buildroot/usr/local/bin
cd %buildroot
# untar it
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
   /usr/local/bin/iR
   /usr/local/bin/iRstudio
   /usr/local/bin/iStata
   /usr/local/bin/iasreml
   /usr/local/bin/imatlab
   /usr/local/bin/imatlab-R2012b
   /usr/local/bin/imatlab-R2013b
   /usr/local/bin/ioctave
   /usr/local/bin/iqsub
   /usr/local/bin/isas
   /usr/local/bin/qR
   /usr/local/bin/qmatlab
   /usr/local/bin/qoctave
   /usr/local/bin/qsas
   /usr/local/bin/qsas_wait
   /usr/local/bin/qstata
   /usr/local/bin/qstata-mp
   /usr/local/bin/qstata-se


%changelog
* Tue Jun 10 2014 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-0
- Initial version
 
