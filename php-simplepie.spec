%define		pkgname		simplepie
%define		php_min_version 5.1.1
%include	/usr/lib/rpm/macros.php
Summary:	SimplePie: Super-fast, easy-to-use, RSS and Atom feed parsing in PHP
Summary(pl.UTF-8):	SimplePie - bardzo szybka, łatwa w użyciu analiza feedów RSS i Atom w PHP
Name:		php-simplepie
Version:	1.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://github.com/rmccue/SimplePie/tarball/%{version}#%{pkgname}-%{version}.tgz
# Source0-md5:	ecf30ac694cedcdc9200b7992ef0bb79
URL:		http://www.simplepie.org/
BuildRequires:	rpm-build >= 4.4.9-96
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	libxml2 >= 1:2.7.2
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-libxml
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-xml
Requires:	php-xmlreader
Suggests:	php-curl
Suggests:	php-idna_convert
Suggests:	php-zlib
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
%setup -qc
mv *-SimplePie-*/* .
mv README.markdown README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a %{pkgname}.inc $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{php_data_dir}/%{pkgname}.inc
