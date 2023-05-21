local sta = require("staline")
  sta.setup({
          	sections = {
		left = {
			' ', 'right_sep_double', '-mode', 'left_sep_double', ' ',
			'right_sep', '-file_name', 'left_sep', ' ',
			'right_sep_double', '-branch', 'left_sep_double', ' ',
		},
		mid  = {'lsp'},
		right= {
			'right_sep', '-cool_symbol', 'left_sep', ' ',
			'right_sep', '- ', '-lsp_name', '- ', 'left_sep',
			'right_sep_double', '-line_column', 'left_sep_double', ' ',
		}
	},

	defaults={
		fg = "#986fec",
		cool_symbol = "  ",
		left_separator = "",
		right_separator = "",
		-- line_column = "%l:%c [%L]",
		true_colors = true,
		line_column = "[%l:%c]  %p%% ",
		-- font_active = "bold"
		        left_separator = "",
        expand_null_ls = false,


        inactive_color = "#303030",
        inactive_bgcolor = "none",
        font_active = "none",          -- bold,italic etc.
        true_colors = false,

        branch_symbol = " ",
        mod_symbol = "  ",
        lsp_client_symbol = " ",
        null_ls_symbol = "",
	},
mode_colors = {
		n  = "#181a23",
		i  = "#181a23",
		ic = "#181a23",
		c  = "#181a23",
		v  = "#181a23",       -- etc
		t  = "#181a23",       -- etc
	}
	,
		mode_icons = {
		n  = " ",
		i  = " ",
		c  = "  ",
		-- a eye symbol for visual mode
		v  =  " " ,      -- etc
		-- a terminal symbol for terminal mode
	},
	-- file_icons = {
	-- 	        typescript=' ' , css=' ' , scss=' ' , javascript=' ' , javascriptreact=' ' , html=' ' ,
    --     python=' ' , java=' ' , markdown=' ' , sh=' ',zsh=' ',
    --     vim=' ', lua=' ', haskell=' ', conf=' ', ruby=' ', txt=' ',
    --     rust=' ', cpp=' ', c=' ', go=' ',
	-- },

	special_table = {
        NvimTree = { 'NvimTree', ' ' },
        packer = { 'Packer','󰏓 ' },
        dashboard = { 'Dashboard', '  ' },
        help = { 'Help', '󰋖 ' },
        qf = { "QuickFix", " " },
        alpha = { "Alpha", "  " },
        Jaq = { "Jaq", "  "},
        Fm = { "Fm", "  "},
        TelescopePrompt = { 'Telescope', "  " },
    },
}
  )
