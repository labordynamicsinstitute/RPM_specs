Name: stattransfer
License: Closed-source
Group: Applications;Statistical
Summary: Stat/Transfer is designed to simplify the transfer of statistical data between different programs.
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 8.1.0.50430
Release: 0 
Source0: ftp://ftp.stattransfer.com/linux/st
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386

%description
Stat/Transfer will automatically read statistical data in the internal format of one of the supported programs and will then transfer as much of the information as is present and appropriate to the internal format of another.

Stat/Transfer preserves all of the precision in your data, while automatically minimizing the size of your output data set.  Stat/Transfer also allows control over the storage format of your output variables.

In addition to converting the formats of variables, Stat/Transfer also processes variable names, missing values and value and variable labels automatically.



%prep

#%setup

%build
rm -f unixman.pdf st st.large.file formats.html
wget ftp://ftp.stattransfer.com/unixman.pdf
wget ftp://ftp.stattransfer.com/linux/st
wget ftp://ftp.stattransfer.com/linux/st.large.file
wget http://www.stattransfer.com/html/formats.html
echo "$(date)
Two binaries are provided by this package. Both are natively compiled on a
i586 machine, they are known to work on a ia64 machine. 

The first binary is the standard Stat/Transfer binary. The second one
has been compiled with large file support.

Please see http://www.stattransfer.com for more details.
" > README.txt

%install
install -d -m 755 %buildroot/usr/local/bin
install -d -m 755 %buildroot/usr/local/stattransfer
for arg in st st.large.file
do
  install -m 755 -g users $arg %buildroot/usr/local/stattransfer
done
cd %buildroot/usr/local/bin
ln -s ../stattransfer/st.large.file st.large.file
ln -s ../stattransfer/st st

%clean
rm -rf %buildroot

%files
/usr/local/bin/st
/usr/local/stattransfer/st
/usr/local/stattransfer/st.large.file
%doc unixman.pdf formats.html README.txt



%changelog 
* Mon Feb 14 2005 Lars Vilhuber
- Embedded the wget commands in spec file
* Sat Feb 12 2005 Lars Vilhuber
- Corrected large file binary
* Fri Feb 11 2005 Lars Vilhuber
- Initial package.


