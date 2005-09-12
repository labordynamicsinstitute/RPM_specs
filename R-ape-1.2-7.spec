########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library ape
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.2
%define packrel  7
%define rel      1
%define packname ape
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL version 2 or newer
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Analyses of Phylogenetics and Evolution
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Ape provides functions for reading, writing, plotting,
and manipulating phylogenetic trees, analyses of comparative data
in a phylogenetic framework, analyses of diversification and
macroevolution, computing distances from allelic and nucleotide
data, reading nucleotide sequences, and several tools such as
Mantel's test, computation of minimum spanning tree, the population
parameter theta based on various approaches, generalized skyline plots,
estimation of absolute evolutionary rates and clock-like
trees using non-parametric rate smoothing, conversion of APE trees
to and from hclust objects and for classifying genes in trees using
the Klastorin-Misawa-Tajima approach.

Author(s)
Emmanuel Paradis <paradis@isem.univ-montp2.fr>,
Korbinian Strimmer <strimmer@stat.uni-muenchen.de>,
Julien Claude <claude@isem.univ-montp2.fr>,
Gangolf Jobb <gangolf.deletethis@treefinder.de>,
Rainer Opgen-Rhein <opgen@stat.uni-muenchen.de>,
Julien Dutheil <julien.dutheil@univ-montp2.fr>,
Yvonnick Noel <noel@univ-lille3.fr>,
Ben Bolker <bolker@zoo.ufl.edu>

2004-09-23

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build
cp %{packname}/DESCRIPTION .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/R/library
%{prefix}/bin/R CMD INSTALL -l $RPM_BUILD_ROOT%{prefix}/lib/R/library %{packname}
%{prefix}/bin/R CMD check %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
%{prefix}/lib/R/library/%{packname}


####### end of spec-file ################################################
