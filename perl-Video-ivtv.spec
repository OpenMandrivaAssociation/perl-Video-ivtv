%define version 0.13
%define release %mkrel 7
%define module	Video-ivtv

Name:		perl-%{module}
Summary:	Perl modules for ivtv support
Group:		Development/Perl
Version:	%{version}
Release:       	%{release}
License:	GPL or Artistic
URL:		http://ivtvdriver.org/
Source0:	http://dl.ivtvdriver.org/supporting-tools/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	perl-devel

%description
Video::ivtv is designed to be a quick hack at making the record_ivtv.pl
script not have to depend on the test_ioctl program included with the ivtv
utils.  By moving to have the things that have proven difficult to do purely
in perl to C where they currently are being done, I can concentrate on
improving the code rather than hitting my head against the wall trying to
do code cleanups.  ;)

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README MANIFEST Changes
%{perl_vendorlib}/*/Video/ivtv.pm
%dir %{perl_vendorlib}/*/Video/
%{perl_vendorlib}/*/auto/Video/ivtv/ivtv.so
%dir %{perl_vendorlib}/*/auto/Video/ivtv/
%dir %{perl_vendorlib}/*/auto/Video/
%{_mandir}/man3/*


