# adjust this upon updates
#boot  class cluster codetools foreign KernSmooth lattice MASS Matrix  mgcv nlme nnet rpart spatial survival 
%define packages abind acepack akima bayesm  car chron  coda    corpcor   DBI  degreenet  delt  denpro  Design   dynamicGraph entropy  ergm  fBasics  fdrtool  feature   gam  GenKern  geoR  ggm   hexbin Hmisc  impute  kernlab ks  latentnet leaps lme4  logspline lpSolve mapproj  maps  maptools  maptree   Matching mclust    MEMSS  mitools misc3d  MKLE  mlmRev  mvtnorm  network  networksis  norm  np  numDeriv  nws  plugdensity  plyr quantreg  R2WinBUGS  RandomFields  randomForest  RArcInfo  rbugs  RColorBrewer   reshape  rgenoud  rgl  Rglpk   rlecuyer  robustbase    rpanel    RSQLite  RUnit  rv sampling samr  SASxport  scatterplot3d  sda  sgeostat  shapes  sm  sna  snow  sp  SparseM  splancs st  statmod  statnet survey  tcltk2  TeachingDemos  timeDate  timeSeries  tkrplot  tree  tripack  tweedie  Umacs  
# The R version should correspond to the R package being installed.
# it will be transformed into an explicit dependency
#removed VR because it was breaking (it is a bundle of other packages MASS class nnet spatial)
%define Rversion 2.9.1 

Name: R-packages-special
License: GPL
Group: Application/Statistics
Summary: R packages for (V)RDC and Hurricane
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: %{Rversion}
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildRequires: R-base >= %{Rversion} 

%if %suse_version >=1000
BuildRequires: gcc-fortran
BuildRequires: gcc-objc gcc gcc-c++
%endif
%if %suse_version < 1000
BuildRequires: gcc-objc gcc gcc-c++
BuildRequires: gcc-g77
%endif

# define the libraries in a subtle manner
%ifarch i586
%define archlib lib
%endif

%ifarch ia64
%define archlib lib
%endif

%ifarch x86_64
%define archlib lib64
%endif


Requires: R-base >= %{Rversion} 
# Update with the relevant packages. So far not automated.
%description
Installs R packages. Currently contains

%{packages}

Note that it is premised on the R package from CRAN (for RHEL5). Mileage with
different R packages (f.i. from EPEL) may vary.

%prep
%setup -n R-packages -c -T
mkdir -p -m 777 %buildroot/usr/%archlib/R/library/
rm -rf %buildroot/usr/%archlib/R/library/*

%build
mkdir -p -m 777 %buildroot/usr/%archlib/R/library/
rm -rf %buildroot/usr/%archlib/R/library/*
pwd
echo "%buildroot" 
for pkg in %{packages}
do
[[ -z $pkgs ]] && pkgs="'$pkg'" || pkgs="$pkgs , '$pkg'"
done
cat > install.R <<EOF
pkgs <- c($pkgs)
install.packages(pkgs, contriburl='http://vrdc3203/cran/src/contrib', lib='%buildroot/usr/%archlib/R/library/') 
EOF
R --vanilla < install.R

# create filelist
[[ -f filelist.R ]] && rm -f filelist.R
for pkg in %{packages}
do
echo "/usr/%archlib/R/library/$pkg" >> filelist.R
done
echo "/usr/%archlib/R/library/R.css" >> filelist.R
 
%install
cd %buildroot
mkdir -p -m 777 %buildroot/usr/%archlib/R/library/

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
rm -r %buildroot

%changelog
* Thu Jul 23 2009 Lars Vilhuber <lv39@vrdc6401.vrdc.cornell.edu> - 2.9.1 -1
- Made the lib references more flexible
- Removed the RHEL reference from the version number - may need to make that more flexible

* Fri Jul 17 2009 Ian Schmutte <ims28@cornell.edu> -2.9.1
-updated spec file to R 2.9.1
-modified package list
-changed references from %buildroot/usr/lib64/ to %buildroot/usr/lib/
* Mon Mar 30 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 2.8.1
- Updated spec file to R 2.8.1

%files -f filelist.R
%defattr(0755,root,root,0755)

