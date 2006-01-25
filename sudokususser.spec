Name: sudokususser
License: tipware
Group: Games
Summary: Sudoku Susser is a free program that helps you play Sudoku
Vendor: Robert Woodhead <trebor@animeigo.com>
URL: http://www.madoverlord.com/projects/sudoku.t
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.0.6
Release: 1
Source0: sudokususser-2.0.6.tgz
#Source1: ftp://ftp.animeigo.com/pub/linuxsusser.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 
Prefix: /opt

%description
The Sudoku Susser is a free program that helps you play Sudoku. If you've been living under a rock and don't know what a Sudoku puzzle is, the London Daily Mail has a good introduction to the puzzles and basic solving techniques. I have also created an introduction to Sudoku puzzles and the basic solving techniques, written for children, which you may find useful. 

%prep
# This might be part of the preparation
# wget %{source1}
# unzip %{source1}
# mv Sudoku.Susser.Linux %{name}-%{version}
# tar czf %{name}-%{version}.tgz %{name}-%{version}
%setup

%build

%install
install -d  -m 755 -o root -p %buildroot/opt/%{name}
install     -m 755 -o root LinuxSusser %buildroot/opt/%{name}/LinuxSusser
install     -m 755 -o root sudokus.txt %buildroot/opt/%{name}/sudokus.txt


#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
#rm -rf %buildroot/opt/softmaker/textmaker

%files
%doc ChangeLog.txt
%doc Sudoku4Kids.pdf
%doc Sudoku\ Susser.pdf
%{prefix}/%{name}/sudokus.txt
%{prefix}/%{name}/LinuxSusser
