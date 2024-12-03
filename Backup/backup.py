import os,zipfile,datetime 

sfondiTeams=r'C:\Users\tl001023\AppData\Roaming\Microsoft\Teams\Backgrounds\Uploads'

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


#print(*searchfiles(".sql","C:\Oracle\dbeaver-ce-6.2.0-win32.win32.x86_64"))

#zipfiles(searchfiles(".sql","C:\Oracle\dbeaver-ce-6.2.0-win32.win32.x86_64"),"backupDbeaverOld.zip")
#zipfiles(searchfiles(".json","C:\Oracle\dbeaver-ce-6.2.0-win32.win32.x86_64"),"backupDbeaverOld.zip",'a')

zipfiles(searchfiles(".ora","C:\Oracle"),"backupOracle.zip")
zipfiles(searchfiles(".pdf","C:\Oracle\Ora2Pg"),"backupOracle.zip",'a')
zipfiles(searchfiles(".txt","C:\Oracle\Ora2Pg"),"backupOracle.zip",'a')
zipfiles(searchfiles(".cmd","C:\Oracle\Ora2Pg"),"backupOracle.zip",'a')
zipfiles(searchfiles(".sql","C:\Oracle\Ora2Pg\out"),"backupOracle.zip",'a')
zipfiles(searchfiles(".conf","C:\Oracle\Ora2Pg\config"),"backupOracle.zip",'a')
zipfiles(searchfiles(".sql","C:\Oracle\DBeaver-22.0.2"),"backupDbeaver.zip")
zipfiles(searchfiles(".json","C:\Oracle\DBeaver-22.0.2"),"backupDbeaver.zip",'a')
zipfiles(searchfiles(".jar","C:\Oracle\DBeaver-22.0.2\drivers"),"backupDbeaver.zip",'a')

zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-1-Esercizio"),"ZZ-SoftwareFactory-1-Esercizio.zip")
zipfiles(searchfiles(".py","C:\ZZ-SoftwareFactory-1-Esercizio"),"ZZ-SoftwareFactory-1-Esercizio.zip",'a')
zipfiles(searchfiles(".txt","C:\ZZ-SoftwareFactory-1-Esercizio"),"ZZ-SoftwareFactory-1-Esercizio.zip",'a')
#zipfiles(searchfiles(".classpath","C:\ZZ-SoftwareFactory-1-Esercizio"),"ZZ-SoftwareFactory-1-Esercizio.zip",'a')
#zipfiles(searchfiles(".project","C:\ZZ-SoftwareFactory-1-Esercizio"),"ZZ-SoftwareFactory-1-Esercizio.zip",'a')

zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip")
zipfiles(searchfiles(".py","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".sh","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".txt","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".cfg","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".xml","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data\\Utility"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".yaml","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".groovy","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".jenkinsfile","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".sql","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data\EstrazioneCasiTest"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".sql","C:\ZZ-SoftwareFactory-0-Sviluppo\Fast Inventory Data\Spool"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".txt","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY\\utility"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".sql","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY\\utility"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".txt","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY\Script"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchnamedfiles("GitManager","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-0-Sviluppo\\DAPHNE"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".sql","C:\ZZ-SoftwareFactory-0-Sviluppo\\DAPHNE\script"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchnamedfiles("note","C:\ZZ-SoftwareFactory-0-Sviluppo\\DAPHNE"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchnamedfiles("GitManager","C:\ZZ-SoftwareFactory-0-Sviluppo\\DAPHNE"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-0-Sviluppo\\SERENA"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".txt","C:\ZZ-SoftwareFactory-0-Sviluppo\\SERENA"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchfiles(".cmd","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY_OLD"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')
zipfiles(searchnamedfiles("GitManager","C:\ZZ-SoftwareFactory-0-Sviluppo\\NUOVO_INVENTORY_OLD"),"ZZ-SoftwareFactory-0-Sviluppo.zip",'a')

zipfiles(["C:\\Users\TL001023\AppData\Local\Microsoft\Edge\\User Data\Default\Bookmarks"],"Bookmark.zip")

#zipfiles(searchfiles(".pdf","C:\Laboratorio"),"Laboratorio.zip",'a')
zipfiles(searchnamedfiles("leggimi","C:\Laboratorio"),"Laboratorio.zip")
zipfiles(searchnamedfiles("note","C:\Laboratorio"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".cmd","C:\Laboratorio"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".go","C:\Laboratorio\GoLang\esempi"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".pdf","C:\Laboratorio\Lua\Documentazione"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".lua","C:\Laboratorio\Lua\esempi"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".lua","C:\Laboratorio\Lua\ZeroBraneStudioEduPack-1.90-win32"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".bas","C:\Laboratorio\BywaterBASIC\esempi"),"Laboratorio.zip",'a')
zipfiles(searchexactfiles("my.ini","C:\Laboratorio\MySql"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".pdf","C:\Laboratorio\Zig"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".pdf","C:\Laboratorio\Scala"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".pdf","C:\Laboratorio\TeaVM"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".scala","C:\Laboratorio\Scala"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".html","C:\Laboratorio\Javascript"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".js","C:\Laboratorio\Javascript"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".css","C:\Laboratorio\Javascript"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".gif","C:\Laboratorio\Javascript"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".cmd","C:\Maven"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".txt","C:\Maven"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".pdf","C:\Maven"),"Laboratorio.zip",'a')
zipfiles(searchnamedfiles("settings","C:\Maven"),"Laboratorio.zip",'a')
zipfiles(searchfiles(".js","C:\Laboratorio\\Node\sample"),"Laboratorio.zip",'a')

zipfiles(searchfiles(".cmd","C:\Applicazioni\Python"),"Applicazioni.zip")
zipfiles(searchfiles(".py","C:\Applicazioni\Python\Script"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".xml","C:\Applicazioni\Lupo_PenSuite_v2016_Zero"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".bat","C:\Applicazioni\SoapUI"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".png","C:\Applicazioni\SoapUI"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".ico","C:\Applicazioni\SoapUI"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".ahk","C:\Applicazioni\DynamicMenu"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".cmd","C:\Applicazioni\DynamicMenu"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".inf","C:\Applicazioni\AutoRun"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".cmd","C:\Applicazioni\AutoRun"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".tlp","C:\Applicazioni\Bitvise Tunnelier"),"Applicazioni.zip",'a')
zipfiles(searchfiles(".cmd","C:\Applicazioni\eclipse"),"Applicazioni.zip",'a')
