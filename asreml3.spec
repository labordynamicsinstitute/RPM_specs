%define rpackage asreml_3.0.1_R_gl-centos5.5-intel64.tar.gz

Name: asreml3
License: Commercial
Group: Application/Statistics
Summary: ASReml is a statistical program for mixed model analysis
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 3.0gm
Release: 1
Source0: asreml-3.0gm-linux-64.tar.gz
Source1: %rpackage
Source2: linux64-install.txt
Source3: install-asreml-R.pdf
Source4: oats.R
Source5: asreml-profile.sh

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

%package R
Group: Application/Statistics
Summary: R package of ASReml 
Requires: asreml3 >= 3.0
%if %{_vendor} == "suse"
Requires: R-base-devel R-base
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
Requires: R-devel R-core
%endif # end of vendor conditions
%description R
This is a virtual package that compiles the R package of ASReml


%prep

%build
cp %{SOURCE2} .
cp %{SOURCE3} .

%install
# directories 
install -d %buildroot/usr/local/bin
install -d %buildroot/opt/asreml3
install -d %buildroot/etc/profile.d

# add the instructions for compiling R package
echo "R CMD INSTALL /opt/asreml3/sources/%rpackage" > installing-R.txt
# add the instructions for removing R package
echo "R CMD REMOVE asreml" > removing-R.txt

# unpack the binary sources
cd %buildroot/opt/asreml3
tar xzvf %{SOURCE0}
# add an example
install %{SOURCE4} %buildroot/opt/asreml3/examples
# adjust the path of the shell
cd bin
mv asreml.sh asreml.tmp
sed 's+/usr/local/asreml3+/opt/asreml3+' asreml.tmp > asreml.sh
chmod a+rx asreml.sh
rm asreml.tmp
# we move the R sources into a subdirectory so that
# the local maintainer can build the R modules, since
# we cannot do it here.
install -d %buildroot/opt/asreml3/sources
install %{SOURCE1} %buildroot/opt/asreml3/sources/

# add the symbolic link
cd %buildroot/usr/local/bin
ln -s ../../../opt/asreml3/bin/asreml.sh  asreml
# add the profile update that points other apps, like the r-asreml
# package, to the license file
install %{SOURCE5} %buildroot/etc/profile.d/

%post

%clean

%post R
# do the R install. Assumes that R is installed
R CMD INSTALL /opt/asreml3/sources/%rpackage

%postun R
R CMD REMOVE asreml

%files
%defattr(-,root,root,-)
/usr/local/bin/asreml
/opt/asreml3
/etc/profile.d/asreml-profile.sh
%doc linux64-install.txt
%doc install-asreml-R.pdf

%files R
%defattr(-,root,root,-)
%doc removing-R.txt
%doc installing-R.txt

%changelog
* Tue Aug 30 2011 lars.vilhuber@cornell.edu
  - Added the profile adjustment and a R example
* Mon Aug 29 2011 lars.vilhuber@cornell.edu
- Initial RPM
