# adjust this upon updates
%define packages Rglpk np Rsymphony R.methodsS3 R.oo
# The R version should correspond to the R package being installed.
# it will be transformed into an explicit dependency
%define Rversion 2.8.1 

Name: R-packages-special
License: GPL
Group: Application/Statistics
Summary: R packages for (V)RDC and Hurricane
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: %{Rversion}
Release: 1.rh5
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildRequires: R >= %{Rversion} gcc-objc++ gcc-gfortran gcc-objc gcc gcc-c++
Requires: R >= %{Rversion} 
# Update with the relevant packages. So far not automated.
%description
Installs R packages. Currently contains

%{packages}

Note that it is premised on the R package from CRAN (for RHEL5). Mileage with
different R packages (f.i. from EPEL) may vary.

%prep
mkdir -p -m 755 %buildroot/usr/lib64/R/library/
\rm -rf %buildroot/usr/lib64/R/library/*
%build
for pkg in %{packages}
do
[[ -z $pkgs ]] && pkgs="'$pkg'" || pkgs="$pkgs , '$pkg'"
done
cat > install.R <<EOF
pkgs <- c($pkgs)
install.packages(pkgs, contriburl='http://vrdc3203/cran/src/contrib', lib='%buildroot/usr/lib64/R/library/') 
EOF
R --vanilla < install.R

# create filelist
[[ -f filelist.R ]] && rm -f filelist.R
for pkg in %{packages}
do
echo "/usr/lib64/R/library/$pkg" >> filelist.R
done
echo "/usr/lib64/R/library/R.css" >> filelist.R
 
%install
cd %buildroot
mkdir -p -m 755 %buildroot/usr/lib64/R/library/

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
rm -r %buildroot/usr/lib64/R/library/

%changelog

* Mon Mar 30 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 2.8.1
- Updated spec file to R 2.8.1

%files -f filelist.R
%defattr(0755,root,root,0755)

