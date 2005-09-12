Name: stata9
License: Commercial
Group: Application/Statistics
Summary: Stata 9 from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 9.0 
Release: 1 
Source0: stata9.installed.tgz 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
Installs Stata. Updated 2005-06-08 from www.stata.com

You still need to install the license, and initialize it. You can initialize the license (as root) by 

cd /usr/local/stata9
./stata
> simulinit
> exit

%prep

%build

%install
cd %buildroot
mkdir -p -m 755 %buildroot/usr/local/bin
tar xzvf %{SOURCE0}  
ln -s ../stata9/stata %buildroot/usr/local/bin/stata9
ln -s ../stata9/stata-se %buildroot/usr/local/bin/stata9-se
ln -s ../stata9/xstata %buildroot/usr/local/bin/xstata9
ln -s ../stata9/xstata-se %buildroot/usr/local/bin/xstata9-se

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata9
fi

%clean
#rm -rf %buildroot/usr/local/stata9

%files
/usr/local/bin/stata9
/usr/local/bin/stata9-se
/usr/local/bin/xstata9
/usr/local/bin/xstata9-se
/usr/local/stata9/ado/
/usr/local/stata9/inst2
/usr/local/stata9/stata
/usr/local/stata9/update_stata
/usr/local/stata9/auto.dta
/usr/local/stata9/setrwxp
/usr/local/stata9/isstata.90
/usr/local/stata9/installed.90
/usr/local/stata9/xstata-se
/usr/local/stata9/stinit
/usr/local/stata9/stata-se
/usr/local/stata9/stata_br
/usr/local/stata9/xstata
/usr/local/stata9/stata.msg
/usr/local/stata9/.license/emptyfile
/usr/local/stata9/.license/stata.sim
/usr/local/stata9/update_stata_se
