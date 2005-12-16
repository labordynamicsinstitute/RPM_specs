Name: asreml
License: Commercial
Group: Application/Statistics
Summary: ASReml is a stastical program for mixed model analysis
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.10
Release: 0
Source0: ASREML110.ia64.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64

%description
ASReml Features

The main features of AS Reml include:

    * Uniquely efficient and fast algorithms for mixed model analysis, saving you considerable time and effort.
    * Handles large data sets (of 100,000 or more observations/effects).
    * Allows for direct fitting of cubic smoothing splines (Verbyla et al, 1999), with user-specified knot points.
    * Facilitates multi-environment trials for the analysis of plant or crop improvement data.
    * Analyses univariate and multivariate breeding and genetics data.
    * Supports a wide range of variance models for spatial analysis.
    * Encourages innovative modelling of longitudinal data. 

AS Reml has already been successfully applied to:

    * Animal and plant breeding and agricultural experimentation
    * Environmental sciences
    * Medical research 
%prep

%build

%install
cd %buildroot
install -d m 755 %buildroot/usr/local/bin
cd %buildroot/usr/local/bin
tar xzf %{SOURCE0}
chmod 0755  %buildroot/usr/local/bin/ASREML110
ln -s ASREML110 asreml

%clean

%files
/usr/local/bin/ASREML110
/usr/local/bin/asreml


%changelog
* Wed Mar 30 2005 vilhuber@lservices
- Initial RPM
