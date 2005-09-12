Name: softmaker-license-ciser
License: Commercial
Group: Application/Office
Summary: Softmaker Office license for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 20050616
Release: 0 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch
Source0: softmaker-extra.tgz

%description
This is CISER's Linux Softmaker Office license. It also contains a customization of the Softmaker config for PDF printing, and a script to propagate the license and config to all accounts.

%prep

%build
#cd %buildroot
tar xzvf %{SOURCE0}

%install
#cd %buildroot/tmp
cd tmp
# licenses and config
install -d m 700 %buildroot/etc/skel/.softmaker
install -m 555 tml.rlx.ciser %buildroot/etc/skel/.softmaker/tml.rlx
install -m 555 pmres04.dat.ciser %buildroot/etc/skel/.softmaker/pmres04.dat
install -m 555 ofl.ini.kprinter %buildroot/etc/skel/.softmaker/ofl.ini
install -m 555 pmconfig.ini.kprinter %buildroot/etc/skel/.softmaker/pmconfig.ini

# tools
install -d m 700 %buildroot/opt/softmaker/sbin
install -m 755 update_softmaker.sh %buildroot/opt/softmaker/sbin/update_softmaker.sh

%clean

%files
%config /etc/skel/.softmaker/ofl.ini
%config /etc/skel/.softmaker/pmconfig.ini
%config /etc/skel/.softmaker/pmres04.dat
%config /etc/skel/.softmaker/tml.rlx
/opt/softmaker/sbin/update_softmaker.sh

%changelog
* Thu Jun 16 2005 lars.vilhuber@cornell.edu
- Initial RPM
