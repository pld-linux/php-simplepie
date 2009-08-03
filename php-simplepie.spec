%define		pkgname		simplepie
Summary:	SimplePie: Super-fast, easy-to-use, RSS and Atom feed parsing in PHP
Summary(pl.UTF-8):	SimplePie - bardzo szybka, łatwa w użyciu analiza feedów RSS i Atom w PHP
Name:		php-simplepie
Version:	1.0.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://www.simplepie.org/downloads/%{pkgname}_%{version}.zip
# Source0-md5:	8c640521de5830fc2d7fe5622cebb71c
URL:		http://www.simplepie.org/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-common >= 3:4.3
Suggests:	php(curl)
Suggests:	php(zlib)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimplePie is a very fast and easy-to-use class, written in PHP, that
puts the 'simple' back into 'really simple syndication'. Flexible
enough to suit beginners and veterans alike, SimplePie is focused on
speed, ease of use, compatibility and standards compliance.

%description -l pl.UTF-8
SimplePie jest bardzo szybką i łatwą w użyciu, napisaną w PHP klasą
umieszczającą "proste" z powrotem do "bardzo prostego zbierania". Jest
wystarczająco elastyczna, aby pasować zarówno początkującym jak i
weteranom. SimplePie skupia się na szybkości, prostocie użycia,
kompatybilności i zgodności ze standardami.

%prep
%setup -q -n 'SimplePie %{version}'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a %{pkgname}.inc $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{php_data_dir}/%{pkgname}.inc
