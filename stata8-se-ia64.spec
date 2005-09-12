Name: stata-se
License: Commercial
Group: Application/Statistics
Summary: Stata 8 SE from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8.2 
Release: 0 
Source0: stata8-se-ia64.tgz 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64 

%description
Installs Stata. You still need to install the license (see stata-ciser-license.rpm), and initialize it. You can initialize the license (as root) by 

cd /usr/local/stata8
./stata
> simulinit
> exit

%prep

%build

%install
cd %buildroot
mkdir -p -m 755 %buildroot/usr/local/bin
tar xzvf %{SOURCE0}  
ln -s ../stata8/stata %buildroot/usr/local/bin/stata
ln -s ../stata8/stata-se %buildroot/usr/local/bin/stata-se
ln -s ../stata8/xstata %buildroot/usr/local/bin/xstata
ln -s ../stata8/xstata-se %buildroot/usr/local/bin/xstata-se

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata8
fi

%clean
#rm -rf %buildroot/usr/local/stata8

%files
/usr/local/bin/stata
/usr/local/bin/stata-se
/usr/local/bin/xstata
/usr/local/bin/xstata-se
/usr/local/stata8/ado/base/
/usr/local/stata8/.license/
/usr/local/stata8/inst2
/usr/local/stata8/stata
/usr/local/stata8/update_stata
/usr/local/stata8/auto.dta
/usr/local/stata8/setrwxp
/usr/local/stata8/isstata.80
/usr/local/stata8/installed.80
/usr/local/stata8/xstata-se
/usr/local/stata8/stinit
/usr/local/stata8/stata-se
/usr/local/stata8/stata_br
/usr/local/stata8/xstata
/usr/local/stata8/update_stata_se

%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
