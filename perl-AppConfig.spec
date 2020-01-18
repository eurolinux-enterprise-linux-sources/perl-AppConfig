Name:           perl-AppConfig
Version:        1.66
Release:        19%{?dist}
Summary:        Perl module for reading configuration files

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/AppConfig/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AB/ABW/AppConfig-%{version}.tar.gz
# Fix documentation, CPAN RT#84318
Patch0:         AppConfig-1.66-Remove-stray-item-from-POD.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long) >= 2.17
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
AppConfig has a powerful but easy to use module for parsing
configuration files.  It also has a simple and efficient module for
parsing command line arguments.  For fully-featured command line
parsing, a module is provided for interfacing AppConfig to Johan
Vromans' extensive Getopt::Long module.  Johan will continue to
develop the functionality of this package and its features will
automatically become available through AppConfig.

# filter out the unversioned provide AppConfig::State from Getopt.pm:
# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^perl(AppConfig::State)$/d
%?perl_default_filter
}
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(AppConfig::State\\)$


%prep
%setup -q -n AppConfig-%{version}
%patch0 -p1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
AUTOMATED_TESTING=1 make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3pm*


%changelog
* Mon Sep  9 2013 Petr Pisar <ppisar@redhat.com> - 1.66-19
- Fix documentation (CPAN RT#84318)

* Mon Nov 05 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-18
- Specify all dependencies
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Mon Aug 20 2012 Daniel Mach <dmach@redhat.com> - 1.66-17.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.66-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 1.66-14
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.66-13
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.66-12
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.66-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.66-9
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.66-8
- Mass rebuild with perl-5.12.0

* Mon Jan 25 2010 Stepan Kasal <skasal@redhat.com> - 1.66-7
- use filtering macros

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.66-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.66-3
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.66-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.66-1
- bump to 1.66

* Thu May 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.65-1
- Update to 1.65.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.64-1
- Update to 1.64.

* Sun Oct  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.63-2
- Excluded the unversioned perl(AppConfig::State) provide.

* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.63-1
- Update to 1.63.
- New upstream maintainer.

* Fri Feb 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.56-4
- Rebuild for FC5 (perl 5.8.8).

* Wed Dec 28 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.56-3
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.56-2
- rebuilt

* Sun May 23 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.56-0.fdr.1
- Update to 1.56.
- License corrected.
- Require perl >= 1:5.6.1 for vendor install dir support.
- Moved make test to section %check.
- Use pure_install to avoid perllocal.pod workarounds.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.55-0.fdr.1
- First build.
