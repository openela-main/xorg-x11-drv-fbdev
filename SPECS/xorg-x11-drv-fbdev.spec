%global tarball xf86-video-fbdev
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

Summary:   Xorg X11 fbdev video driver
Name:      xorg-x11-drv-fbdev
Version:   0.5.0
Release:   11%{?dist}
URL:       http://www.x.org
License:   MIT

Source0:   https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

Patch0: 0001-mustard-Enable-linking-with-z-now.patch
Patch2: BGNoneRoot.patch

BuildRequires: make
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: autoconf automake libtool

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 fbdev video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1
%patch2 -p1

%build
autoreconf -vif
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/fbdev_drv.so
%{_mandir}/man4/fbdev.4*

%changelog
* Wed Feb 23 2022 Adam Jackson <ajax@redhat.com> - 0.5.0-11
- Enable hardened build
  Resolves: rhbz#2044899

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.5.0-10
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.5.0-9
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 09:57:16 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.0-7
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Adam Jackson <ajax@redhat.com> - 0.5.0-1
- fbdev 0.5.0

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 0.4.3-30
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 0.4.3-25
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 0.4.3-23
- 1.15 ABI rebuild

* Tue Jun 23 2015 Adam Jackson <ajax@redhat.com> - 0.4.3-22
- Undefine _hardened_build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 0.4.3-20
- xserver 1.17 ABI rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 0.4.3-18
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 0.4.3-16
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 0.4.3-15
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 0.4.3-14
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 0.4.3-13
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 0.4.3-12
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 0.4.3-11
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 0.4.3-9
- autoreconf for aarch64

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.3-8
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.3-7
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.3-6
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.3-5
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 0.4.3-4
- ABI rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> - 0.4.3-2
- ABI rebuild

* Mon Jul 02 2012 Dave Airlie <airlied@redhat.com> 0.4.3-1
- upstream 0.4.3 release

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 0.4.2-9
- RHEL arch exclude updates

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.2-8
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.2-7
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.2-6
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.2-5
- Rebuild for server 1.12

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-4
- ABI rebuild

* Wed Nov 09 2011 ajax <ajax@redhat.com> - 0.4.2-3
- ABI rebuild

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-2
- Rebuild for xserver 1.11 ABI

* Tue Jun 21 2011 Adam Jackson <ajax@redhat.com> 0.4.2-1
- fbdev 0.4.2

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.1-9
- Rebuild for server 1.11

* Tue Mar 01 2011 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.1-8
- Rebuild for server 1.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Dave Airlie <airlied@redhat.com> 0.4.1-6
- fix bg none root

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 0.4.1-5
- Add ABI requires magic. (#542742)

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.1-4
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.1-3
- Rebuild for server 1.8

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.1-2
- Rebuild for server 1.8

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 0.4.1-1
- fbdev 0.4.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.4.0-5.1
- ABI bump

* Mon Jun 22 2009 Peter Hutterer <peter.hutterer@redhat.com> 0.4.0-5
- fbdev-0.4.0-Make-ISA-optional.patch: to make next patch apply cleanly.
- fbdef-0.4.0-Remove-useless-loader-symbol-lists.patch:
  fix linker error against X server >= 1.6.99.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 0.4.0-3
- rebuild for latest server API

* Thu Oct 30 2008 Bill Nottingham <notting@redhat.com> 0.4.0-2
- set canDoBGNoneRoot on driver startup

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.4.0-1
- Update to latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-7
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 0.3.1-6
- rebuild for abi change.

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 0.3.1-5.20071113
- Update to git snapshot for pciaccess goodness.  Don't ask why a driver
  that doesn't touch PCI at all needs a PCI update.  I don't know either,
  and thinking about it makes me very sad.
- Require xserver 1.4.99.1

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.3.1-4
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.3.1-3
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.3.1-2
- ExclusiveArch -> ExcludeArch

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 0.3.1-1
- Update to 0.3.1

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.3.0-2
- adjust to prefer 32bpp over 24bpp for fbbpp (#204117)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.3.0-1
- Update to 0.3.0 from 7.1.

* Tue May 16 2006 Adam Jackson <ajackson@redhat.com> 0.2.0-2
- Move debugging output from compile-time option to run-time option.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.2.0-1
- Update to 0.2.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.1.0.5-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.4-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.2-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 0.1.0.1-1
- Updated xorg-x11-drv-fbdev to version 0.1.0.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 0.1.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Add alpha/sparc/sparc64 to "ExclusiveArch"

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 0.1.0-0
- Initial spec file for fbdev video driver generated automatically
  by my xorg-driverspecgen script.
