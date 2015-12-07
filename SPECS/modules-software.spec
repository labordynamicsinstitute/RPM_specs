Name: modules-software
License: GPLv3
Group: Application/Statistics
Summary: Module packages for specific software installations. May not be generalizable
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.0
Release: 0
Source0: Modules.ampl.tgz
Source1: Modules.knitro.tgz
Source2: Modules.matlab-R2012b.tgz
Source3: Modules.matlab-R2013b.tgz
Source4: Modules.matlab-R2014b.tgz
Source5: Modules.matlab-R2015b.tgz
Source6: Modules.R-ACML.tgz
Source7: Modules.R-MKL.tgz
Source8: Modules.R-RPM.tgz
Source9: Modules.SAS-9.4.tgz
Source10: Modules.stata12.tgz
Source11: Modules.stata13.tgz
Source12: Modules.stata14.tgz
Source13: Modules.ox-7.tgz
Source14: Modules.python-anaconda.tgz

BuildArch: noarch
%if %{_vendor} == "suse"
Requires: Modules
BuildRequires: Modules
%else
# applies to RHEL systems, not testing for any other systems
BuildRequires: environment-modules
Requires: environment-modules
%endif # end of else/RHEL condition

%description
This packages modules commands for different software pieces that might be installed.
The package does not check that the software is actually installed.

# ls -1 Modules.* | awk -F. ' { print "%package " $2 "\nGroup: Application/Statistics\nSummary: Module files for " $2 "\n%description " $2 "\nModule files for " $2  "\n"} '
%package ampl-20150516
Group: Application/Statistics
Summary: Module files for ampl
%description ampl-20150516
Module files for ampl

%package ampl-20150516-default
Group: Application/Statistics
Summary: Sets this version of ampl to be default
%description ampl-20150516-default
 Sets this version of ampl to be default

%package knitro-9.1.0-z
Group: Application/Statistics
Summary: Module files for knitro
%description knitro-9.1.0-z
Module files for knitro

%package knitro-9.1.0-z-default
Group: Application/Statistics
Summary: Sets this version of knitro to be default
%description knitro-9.1.0-z-default
Sets this version of knitro to be default

%package matlab-R2012b
Group: Application/Statistics
Summary: Module files for matlab-R2012b
%description matlab-R2012b
Module files for matlab-R2012b

%package matlab-R2013b
Group: Application/Statistics
Summary: Module files for matlab-R2013b
%description matlab-R2013b
Module files for matlab-R2013b

%package matlab-R2014b
Group: Application/Statistics
Summary: Module files for matlab-R2014b
%description matlab-R2014b
Module files for matlab-R2014b

%package matlab-R2015b
Group: Application/Statistics
Summary: Module files for matlab-R2015b
%description matlab-R2015b
Module files for matlab-R2015b

%package matlab-R2015b-default
Group: Application/Statistics
Summary: Set this to be the default version
%description matlab-R2015b-default
Set this to be the default version

%package R-ACML
Group: Application/Statistics
Summary: Module files for R-ACML
%description R-ACML
Module files for R-ACML

%package R-MKL
Group: Application/Statistics
Summary: Module files for R-MKL
%description R-MKL
Module files for R-MKL

%package R-RPM
Group: Application/Statistics
Summary: Module files for R-RPM
%description R-RPM
Module files for R-RPM

%package SAS-9
Group: Application/Statistics
Summary: Module files for SAS-9
%description SAS-9
Module files for SAS-9

%package SAS-9-default
Group: Application/Statistics
Summary: Set this version of SAS to be default
%description SAS-9-default
Set this version of SAS to be default

%package stata12
Group: Application/Statistics
Summary: Module files for stata12
%description stata12
Module files for stata12

%package stata13
Group: Application/Statistics
Summary: Module files for stata13
%description stata13
Module files for stata13

%package stata14
Group: Application/Statistics
Summary: Module files for stata14
%description stata14
Module files for stata14

%package stata14-default
Group: Application/Statistics
Summary: Set this version of stata to be the default version
%description stata14-default
Set this version of stata to be the default version

%package ox-7
Group: Application/Statistics
Summary: Module files for Ox 7
%description ox-7
Module files for Ox 7

%package python-anaconda
Group: Application/Statistics
Summary: Module files for Python by Anaconda
%description python-anaconda
Module files for Python by Anaconda. Requires at least some configuration.

%package python-anaconda-3.3
Group: Application/Statistics
Summary: Module files for Python by Anaconda
%description python-anaconda-3.3
Module files for Python by Anaconda. Requires at least some configuration.




%build
#cd %buildroot
echo "This is a placeholder package" > README


%install
#cd %buildroot
install -d m 755 %buildroot/usr/share/Modules/modulefiles
cd %buildroot/usr/share/Modules/modulefiles
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
tar xzvf %{SOURCE2}
tar xzvf %{SOURCE3}
tar xzvf %{SOURCE4}
tar xzvf %{SOURCE5}
tar xzvf %{SOURCE6}
tar xzvf %{SOURCE7}
tar xzvf %{SOURCE8}
tar xzvf %{SOURCE9}
tar xzvf %{SOURCE10}
tar xzvf %{SOURCE11}
tar xzvf %{SOURCE12}
tar xzvf %{SOURCE13}
tar xzvf %{SOURCE14}

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%dir /usr/share/Modules/
%dir /usr/share/Modules/modulefiles/
%dir /usr/share/Modules/modulefiles/stata/
%dir /usr/share/Modules/modulefiles/stata/mp
%dir /usr/share/Modules/modulefiles/stata/se
%dir /usr/share/Modules/modulefiles/matlab/
%dir /usr/share/Modules/modulefiles/R/
%dir /usr/share/Modules/modulefiles/ox/
%dir /usr/share/Modules/modulefiles/python/
%doc README


%files ampl-20150516
%dir /usr/share/Modules/modulefiles/ampl/
/usr/share/Modules/modulefiles/ampl/20150516

%files ampl-20150516-default
/usr/share/Modules/modulefiles/ampl/.version

%files knitro-9.1.0-z
%dir /usr/share/Modules/modulefiles/knitro/
/usr/share/Modules/modulefiles/knitro/9.1.0-z

%files knitro-9.1.0-z-default
/usr/share/Modules/modulefiles/knitro/.version

%files matlab-R2012b
/usr/share/Modules/modulefiles/matlab/R2012b

%files matlab-R2013b
/usr/share/Modules/modulefiles/matlab/R2013b

%files matlab-R2014b
/usr/share/Modules/modulefiles/matlab/R2014b

%files matlab-R2015b
/usr/share/Modules/modulefiles/matlab/R2015b

%files matlab-R2015b-default
/usr/share/Modules/modulefiles/matlab/.version

%files R-ACML
%dir /usr/share/Modules/modulefiles/R/ACML/
%dir /usr/share/Modules/modulefiles/R/ACML/MP/
/usr/share/Modules/modulefiles/R/ACML/3.2.0
/usr/share/Modules/modulefiles/R/ACML/3.0.2
/usr/share/Modules/modulefiles/R/ACML/MP/3.2.0
/usr/share/Modules/modulefiles/R/ACML/MP/3.0.2
/usr/share/Modules/modulefiles/R/ACML/.version

%files R-MKL
%dir /usr/share/Modules/modulefiles/R/MKL/
%dir /usr/share/Modules/modulefiles/R/MKL/MP/
/usr/share/Modules/modulefiles/R/MKL/3.0.2
/usr/share/Modules/modulefiles/R/MKL/.modulerc
/usr/share/Modules/modulefiles/R/MKL/MP/3.0.2
/usr/share/Modules/modulefiles/R/MKL/.version

%files R-RPM
/usr/share/Modules/modulefiles/R/3.2.2

%files SAS-9
%dir /usr/share/Modules/modulefiles/sas/
/usr/share/Modules/modulefiles/sas/9.4

%files SAS-9-default
/usr/share/Modules/modulefiles/sas/.version

%files stata12
/usr/share/Modules/modulefiles/stata/12
/usr/share/Modules/modulefiles/stata/mp/12
/usr/share/Modules/modulefiles/stata/se/12

#%files stata12-default

%files stata13
/usr/share/Modules/modulefiles/stata/13
/usr/share/Modules/modulefiles/stata/mp/13
/usr/share/Modules/modulefiles/stata/se/13

#%files stata13-default

%files stata14
/usr/share/Modules/modulefiles/stata/14
/usr/share/Modules/modulefiles/stata/mp/14
/usr/share/Modules/modulefiles/stata/se/14

%files stata14-default
/usr/share/Modules/modulefiles/stata/.version
/usr/share/Modules/modulefiles/stata/mp/.version
/usr/share/Modules/modulefiles/stata/se/.version

%files ox-7
/usr/share/Modules/modulefiles/ox/.version
/usr/share/Modules/modulefiles/ox/7.0

%files python-anaconda
%dir /usr/share/Modules/modulefiles/python/anaconda
/usr/share/Modules/modulefiles/python/.version
/usr/share/Modules/modulefiles/python/2.6
/usr/share/Modules/modulefiles/python/anaconda/2.7
/usr/share/Modules/modulefiles/python/anaconda/.version

%files python-anaconda-3.3
/usr/share/Modules/modulefiles/python/anaconda/3.3


%changelog

* Mon Dec 7 2015 lars.vilhuber@cornell.edu
- Initial RPM
