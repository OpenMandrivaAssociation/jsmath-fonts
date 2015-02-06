Name:		jsmath-fonts
Version:	3.0
Release:	3
License:	Freeware
Summary:	jsMath TrueType fonts

Source:		http://www.math.union.edu/~dpvc/jsMath/download/TeX-fonts-linux.tgz
BuildArch:	noarch
URL:		http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html

%description
The jsMath package is designed to work best if you have installed the TeX
font set. This package provides a set of TeX ttf fonts for Linux systems.

%prep
%setup -q -n TeX-fonts-linux

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/jsMath
install -m644 *.ttf %{buildroot}%{_datadir}/fonts/jsMath

%files
%dir %{_datadir}/fonts/jsMath
%{_datadir}/fonts/jsMath/*.ttf
