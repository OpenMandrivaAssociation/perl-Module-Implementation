%define modname	Module-Implementation
%define modver 0.07

Summary:	Loads one of several alternate underlying implementations for a module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-Implementation-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl-devel

%description
This module abstracts out the process of choosing one of several underlying
implementations for a module. This can be used to provide XS and pure Perl
implementations of a module, or it could be used to load an implementation
for a given OS or any other case of needing to provide multiple
implementations.

This module is only useful when you know all the implementations ahead of
time. If you want to load arbitrary implementations then you probably want
something like a plugin system, not this module.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE META.yml Changes META.json INSTALL
%{perl_vendorlib}/*
%{_mandir}/man3/*


