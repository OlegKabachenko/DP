class Config():  
    app_wide_scr_mult = 1.2 #the app window is considered wide when wide*app_wide_scr_mult > height

    #------for text in select formula/method area
    sfm_narrow_fnt_mult = 0.08#font multiplier when app window is narrow
    sfm_wide_fnt_mult = 0.65 #font multiplier when app window is wide

    sfm_critical_width = 360 #size that is considered very narrow
    sfm_extra_fnt_mult = 1.4 #multiplayer to increase font size when application window is too narrow
    
    sfm_max_font_corr = 0.5 # the maximum % of the base font that the font_corrector can be equal to
        
    sfm_corr_wide_divider = 2.5#font correction divider when app window is wide
    sfm_corr_narrow_divider = 6#font correction divider when app window is narrow

    #------for drop menu
    menu_item_narrow_fnt_mult = 25#font multiplier when app window is narrow(for items in dropmenu)
    menu_item_wide_fnt_mult = 20 #font multiplier when app window is wide(for items in dropmenu)

    #------for integral parameters layout
    p_widg_wide_item_mult = 2 #widget of integral parameter is considered  wide when width*p_widg_wide_item_mult > height
    p_font_wide_wid_mult = 0.3 #used when calculating font size for integral parameter widget when parent widget is wide       
    p_font_narrow_wid_mult = 7  #used when calculating font size for integral parameter widget when parent widget is narrow
    p_section_height = 80
    p_section_wide_scr_mult = 1 #used to select the appropriate orientation for parameter section 
        
    def __init__(self):        
        self.card_l_color = self.normalize_rgb(221, 249, 255)       
                  
    def normalize_rgb (self, r, g, b): 
        r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
        return [r/255, g/255, b/255]        
