Name: 3ware_7xxx
License: Commercial
Group: System
Summary: Installs the 3Ware 7000 series CLI, documentation, firmware
Packager: Lars Vilhuber <lars.vilhuber@cloutier-vilhuber.net>
Version: 9.3.0.3
Release: 1 
Source0: tw_cli-linux-x86-%{version}.tgz
Source1: 3ware_7xxx.doc.tgz
Source2: 3ware_7xxx.fw.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386

%description
Installs the 3Ware 7000/8000 Series CLI, provides documentation and firmware
It does not provide or install the 3DM web interface. This may be needed
for newer 7xxx or 8xxx hardware, and might work for the 9000 hardware as well.

%prep

%build
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
cp %{SOURCE2} .

%install
install -d -m 755 %buildroot/usr/local/sbin
install -m 755 -o root -g root tw_cli %buildroot/usr/local/sbin 
install -m 755 -o root -g root tw_sched %buildroot/usr/local/sbin 
install -d -m 755 %buildroot/usr/local/man/man8
install -m 755 -o root -g root tw_cli.8.nroff %buildroot/usr/local/man/man8/tw_cli.8
install -m 755 -o root -g root tw_sched.8.nroff %buildroot/usr/local/man/man8/tw_sched.8


%clean
rm -rf %buildroot

%files
/usr/local/sbin/tw_cli
/usr/local/sbin/tw_sched
/usr/local/man/man8/tw_cli.8.gz
/usr/local/man/man8/tw_sched.8.gz
%doc EscaladeUG7000-122003.pdf Escalade7000IG_042903.pdf Escalade7xxx_CLI_UG.pdf 3ware_7xxx.fw.zip tw_sched.cfg tw_cli.8.html tw_sched.8.html


%changelog 
* Mon Mar 20 2006 - lars.vilhuber@cornell.edu
- Updated with newer software (the old didn't recognize a newly bought 7506 controller)
* Wed May 20 2005 - lars.vilhuber@cornell.edu
- Initial build.
- You have to download all these files from the 3Ware website.

