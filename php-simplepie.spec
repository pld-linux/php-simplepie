%define		pkgname		simplepie
%define		php_min_version 5.1.1
%include	/usr/lib/rpm/macros.php
Summary:	SimplePie: Super-fast, easy-to-use, RSS and Atom feed parsing in PHP
Summary(pl.UTF-8):	SimplePie - bardzo szybka, łatwa w użyciu analiza feedów RSS i Atom w PHP
Name:		php-simplepie
Version:	1.2.1
Release:	5
License:	New BSD
Group:		Development/Languages/PHP
Source0:	https://nodeload.github.com/simplepie/simplepie/tarball/%{version}?/%{pkgname}-%{version}.tgz
# Source0-md5:	1ed5e112c9b2f97699d1096d4ee4c52b
Patch0:		build.patch
Patch1:		php5.3-notices.patch
URL:		http://www.simplepie.org/
BuildRequires:	rpm-build >= 4.4.9-96
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	libxml2 >= 1:2.7.2
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(xml)
Suggests:	php-curl
Suggests:	php-idna_convert
# MySQL for cache
Suggests:	php-mysql
Suggests:	php-xmlreader
Suggests:	php-zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional php dependencies
%define		_noautophp	php-mysql php-curl php-zlib php-xmlreader

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

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
mv *-simplepie-*/* .
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p %{pkgname}.inc $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%{php_data_dir}/%{pkgname}.inc
