def null_upgrade_step(setup_tool):
    """
    This is a null upgrade. Use it when nothing happens.
    """
    pass
    
def upgrade_to_20b1(setup_tool):
    """
    Upgrade the pre-GenericSetup version of Scrawl to version 2.0b1.
    """
    
    profile = 'profile-Products.Scrawl:upgrade_to_20b1'
    setup_tool.runAllImportStepsFromProfile(profile)