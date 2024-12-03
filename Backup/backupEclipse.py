import os,zipfile,datetime 

def searchfiles(extension='.txt', folder='C:\\'):
     f = []
     for (dirpath, dirnames, filenames) in os.walk(folder):
          f.extend(os.path.join(dirpath, filename) for filename in filenames if filename.endswith(extension))
     return f

def searchnamedfiles(name='leggimi', folder='C:\\'):
     f = []
     for (dirpath, dirnames, filenames) in os.walk(folder):
          f.extend(os.path.join(dirpath, filename) for filename in filenames if filename.startswith(name))
     return f

def searchexactfiles(name='leggimi.txt', folder='C:\\'):
     f = []
     for (dirpath, dirnames, filenames) in os.walk(folder):
          f.extend(os.path.join(dirpath, filename) for filename in filenames if filename.startswith(name))
     return f


def zipfiles(tozip, name="backup.zip", mode='w'):
     with zipfile.ZipFile(name,mode) as myzip:
          for file in tozip:
               myzip.write(file)
     myzip.close()


zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-RISO"),"Workspace-RISO.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-RISO"),"Workspace-RISO.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-RISO"),"Workspace-RISO.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-RISO"),"Workspace-RISO.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-RISO"),"Workspace-RISO.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-CViewer"),"Workspace-CViewer.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-CViewer"),"Workspace-CViewer.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-CViewer"),"Workspace-CViewer.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-CViewer"),"Workspace-CViewer.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-CViewer"),"Workspace-CViewer.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-OPI"),"Workspace-OPI.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-OPI"),"Workspace-OPI.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-OPI"),"Workspace-OPI.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-OPI"),"Workspace-OPI.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-OPI"),"Workspace-OPI.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5"),"Workspace-MyDynamic-5.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5"),"Workspace-MyDynamic-5.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5"),"Workspace-MyDynamic-5.zip",'a')
zipfiles(searchfiles(".java","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5\MyDynamicEntities"),"Workspace-MyDynamic-5.zip",'a')
zipfiles(searchfiles(".java","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5\MyDynamicTest"),"Workspace-MyDynamic-5.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5"),"Workspace-MyDynamic-5.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-MyDynamic-5"),"Workspace-MyDynamic-5.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Dati"),"Workspace-Dati.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Dati"),"Workspace-Dati.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Dati"),"Workspace-Dati.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Dati"),"Workspace-Dati.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Dati"),"Workspace-Dati.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-SOA"),"Workspace-SOA.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-SOA"),"Workspace-SOA.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-SOA"),"Workspace-SOA.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-SOA"),"Workspace-SOA.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-SOA"),"Workspace-SOA.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-DECO"),"Workspace-DECO.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-DECO"),"Workspace-DECO.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-DECO"),"Workspace-DECO.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-DECO"),"Workspace-DECO.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-DECO"),"Workspace-DECO.zip",'a')

zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Servizi"),"Workspace-Servizi.zip")
zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Servizi"),"Workspace-Servizi.zip",'a')
zipfiles(searchnamedfiles("org.eclipse.jdt.core.prefs","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Servizi"),"Workspace-Servizi.zip",'a')
zipfiles(searchnamedfiles("log4j.xml","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Servizi"),"Workspace-Servizi.zip",'a')
zipfiles(searchfiles(".properties","C:\ZZ-SoftwareFactory-1-Esercizio\Workspace-Servizi"),"Workspace-Servizi.zip",'a')





