Name: asreml3
License: Commercial
Group: Application/Statistics
Summary: ASReml is a statistical program for mixed model analysis
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 3.0gm
Release: 1
Source0: asreml-3.0gm-linux-64.tar.gz
Source1: asreml_3.0.1_R_gl-centos5.5-intel64.tar.gz
Source2: linux64-install.txt
Source3: install-asreml-R.pdf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


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
# directories 
install -d %buildroot/usr/local/bin
install -d %buildroot/opt/asreml3
cd %buildroot/opt/asreml3
tar xzvf %{SOURCE0}
cd bin
mv asreml.sh asreml.tmp
sed 's+/usr/local/asreml3+/opt/asreml3+' asreml.tmp > asreml.sh
chmod a+rx asreml.sh
rm asreml.tmp
cd %buildroot/usr/local/bin
ln -s ../../../opt/asreml3/bin/asreml.sh  asreml

%clean

%files
%defattr(-,root,root,-)
/usr/local/bin/asreml
/opt/asreml3
%doc linux64-install.txt
%doc install-asreml-R.pdf



%changelog
* Mon Aug 29 2011 lars.vilhuber@cornell.edu
- Initial RPM