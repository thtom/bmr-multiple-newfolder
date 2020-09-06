 #!/usr/bin/env python
def execute():

    for i in range(10, 22):

        mp = proj.GetMediaPool()  
        folder  = mp.GetRootFolder()
        mp.AddSubFolder(folder, "sc" + str(i))
        folder = mp.GetCurrentFolder()

if __name__ == '__main__':

    # Instantiate Resolve objects
    import DaVinciResolveScript as dvr_script
    resolve = dvr_script.scriptapp("Resolve")
    pm      = resolve.GetProjectManager()
    proj    = pm.GetCurrentProject()
    mp      = proj.GetMediaPool()
    folder  = mp.GetRootFolder()
    clips   = folder.GetClips()
    
    execute()
