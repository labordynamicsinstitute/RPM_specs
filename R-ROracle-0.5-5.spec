########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library ROracle
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.5
%define packrel  5
%define rel      1
%define packname ROracle
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: LGPL version 2 or newer
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Oracle database interface for R
BuildRequires: R-base
PreReq: R-base
Requires:  R-DBI
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Oracle database interface (DBI) driver for R.
This is a DBI-compliant Oracle driver based on the ProC/C++
embedded SQL.  It implements the DBI version 0.1-4 plus one
extension.

Author(s)
David A. James <dj@bell-labs.com>
Jake Luciani <jakeluciani@yahoo.com>

2004-06-21

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
