%define upstream_version 0.13
%define module	Video-ivtv

Name:		perl-%{module}
Summary:	Perl modules for ivtv support
Group:		Development/Perl
Version:	%perl_convert_version %{upstream_version}
Release:    2
License:	GPL or Artistic
URL:		http://ivtvdriver.org/
Source0:	http://dl.ivtvdriver.org/supporting-tools/Video-ivtv-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

%description
Video::ivtv is designed to be a quick hack at making the record_ivtv.pl
script not have to depend on the test_ioctl program included with the ivtv
utils.  By moving to have the things that have proven difficult to do purely
in perl to C where they currently are being done, I can concentrate on
improving the code rather than hitting my head against the wall trying to
do code cleanups.  ;)

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
#make test

%install
%{makeinstall_std}

%files
%doc README MANIFEST Changes
%{perl_vendorlib}/*/Video/ivtv.pm
%dir %{perl_vendorlib}/*/Video/
%{perl_vendorlib}/*/auto/Video/ivtv/ivtv.so
%dir %{perl_vendorlib}/*/auto/Video/ivtv/
%dir %{perl_vendorlib}/*/auto/Video/
%{_mandir}/man3/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.13-10mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.13-9mdv2011.0
+ Revision: 556190
- rebuild for perl 5.12

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.13-8mdv2010.0
+ Revision: 440743
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.13-7mdv2009.1
+ Revision: 350219
- 2009.1 rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.13-6mdv2009.0
+ Revision: 258757
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-5mdv2009.0
+ Revision: 246694
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2008.1
+ Revision: 152386
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.13-2mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.13-2mdv2007.0
+ Revision: 103841
- Import perl-Video-ivtv

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.13-2mdk
- Rebuild
- %%mkrel
- update URLs

* Wed Nov 17 2004 Stefan van der Eijk <stefan@mandrake.org> 0.13-1mdk
- 0.13

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.12-5mdk
- Rebuild for new perl

* Fri Jun 25 2004 Stefan van der Eijk <stefan@mandrake.org> 0.12-4mdk
- initial Mandrake package
- License
- Requires


