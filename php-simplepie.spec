Summary:	SimplePie: Super-fast, easy-to-use, RSS and Atom feed parsing in PHP
Name:		simplepie
Version:	1.0.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://simplepie.org/downloads/%{name}_%{version}.zip
# Source0-md5:	8c640521de5830fc2d7fe5622cebb71c
URL:		http://simplepie.org/
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-common >= 3:4.3
Suggests:	php(curl)
Suggests:	php(zlib)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir	/usr/share/php

%description
SimplePie is a very fast and easy-to-use class, written in PHP, that
puts the 'simple' back into 'really simple syndication'. Flexible
enough to suit beginners and veterans alike, SimplePie is focused on
speed, ease of use, compatibility and standards compliance.

%prep
%setup -q -n "SimplePie\ %{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}
cp -a simplepie.inc $RPM_BUILD_ROOT%{_phpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_phpdir}/simplepie.inc
