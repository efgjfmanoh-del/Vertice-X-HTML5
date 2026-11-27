import pathlib,re,xml.etree.ElementTree as ET
p=pathlib.Path('android/app/src/main/AndroidManifest.xml')
s=p.read_text()
s=s.replace('android:icon="@mipmap/ic_launcher"','android:icon="@drawable/vx_icon"').replace('android:roundIcon="@mipmap/ic_launcher_round"','android:roundIcon="@drawable/vx_icon"')
s=s.replace('android:launchMode="singleTask"','android:launchMode="singleTask" android:screenOrientation="landscape"')
p.write_text(s)
root=ET.fromstring(s)
ns='{http://schemas.android.com/apk/res/android}'
assert root.find('application').get(ns+'icon')=='@drawable/vx_icon'
assert any(a.get(ns+'screenOrientation')=='landscape' for a in root.findall('application/activity'))
d=p.parent/'res/drawable';d.mkdir(parents=True,exist_ok=True)
(d/'vx_icon.xml').write_text("""<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="108dp" android:height="108dp" android:viewportWidth="512" android:viewportHeight="512">
<path android:fillColor="#101D33" android:pathData="M0,0 L512,0 L512,512 L0,512 Z"/>
<path android:fillColor="#00000000" android:strokeColor="#54D9E7" android:strokeWidth="9" android:pathData="M256,50 L453,256 L256,462 L59,256 Z"/>
<path android:fillColor="#B0EAFA" android:pathData="M91,144 L155,144 L224,310 L192,383 Z"/>
<path android:fillColor="#F45E72" android:pathData="M417,120 L344,120 L241,232 L171,120 L99,120 L202,286 L126,392 L205,392 L258,328 L310,392 L390,392 L294,282 Z"/>
<path android:fillColor="#FFFFFF" android:pathData="M256,65 L271,92 L256,120 L241,92 Z"/>
</vector>""")
g=pathlib.Path('android/app/build.gradle');t=g.read_text()
t,n=re.subn(r'versionName\s+"[^"]+"','versionName "0.1.0"',t);assert n==1
g.write_text(t)
