Name: 3ware_7xxx
License: Commercial
Group: System
Summary: Installs the 3Ware 7000 series CLI, documentation, firmware
Packager: Lars Vilhuber <lars.vilhuber@cloutier-vilhuber.net>
Version: 7.7.1 
Release: 1 
Source0: cli_linux.tgz
Source1: 3ware_7xxx.doc.tgz
Source2: 3ware_7xxx.fw.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386

%description
Installs the 3Ware 7000 Series CLI, provides documentation and firmware
It does not provide or install the 3DM web interface.

%prep

%build
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
cp %{SOURCE2} .

%install
install -d -m 755 %buildroot/usr/local/sbin
install -m 755 -o root -g root tw_cli %buildroot/usr/local/sbin 

%clean
rm -rf %buildroot

%files
/usr/local/sbin/tw_cli
%doc EscaladeUG7000-122003.pdf Escalade7000IG_042903.pdf Escalade7xxx_CLI_UG.pdf 3ware_7xxx.fw.zip


%changelog 
* Wed May 20 2005 - lars.vilhuber@cornell.edu
- Initial build.
- You have to download all these files from the 3Ware website.

