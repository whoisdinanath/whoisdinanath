vim.g.mapleader = " "

local map = function(mode, lhs, rhs, opts)
    local options = {noremap = true, silent = true}
    if opts then
        options = vim.tbl_extend("force", options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

-- Navigation keys in insert mode
map("i", "<C-h>", "<Left>")
map("i", "<C-j>", "<Down>")
map("i", "<C-k>", "<Up>")
map("i", "<C-l>", "<Right>")

-- Normal mode other keys
map("n", "<C-s>", ":w <CR>")
map("n", "<C-q>", ":bd!<CR>")

-- Bufferline --
map("n", "<TAB>", ":BufferLineCycleNext<CR>")
map("n", "<S-TAB>", ":BufferLineCyclePrev<CR>")

-- Nvim tree
map("n", "<leader>a", ":NvimTreeToggle<CR>")

-- muscle memory escape to jj
map("i", "jj", "<ESC>")

-- Telescope
map("n", "<leader>F", ":Telescope find_files <CR>")
map("n", "<leader>fl", ":Telescope live_grep <CR>")
map("n", "<leader>th", ":Telescope colorscheme  <CR>")
map("n", "<leader>b", ":Telescope buffers<CR>")

-- Window splitting
map("n", "<leader>v", ":vsplit<CR>")
map("n", "<leader>h", ":split<CR>")
map("n", "<leader>q", ":q<CR>")
map("n", "<leader>o", ":only<CR>")
map("n", "<leader>=", ":resize +5<CR>")
map("n", "<leader>-", ":resize -5<CR>")
map("n", "<leader>+", ":vertical resize +5<CR>")
map("n", "<leader>_", ":vertical resize -5<CR>")

--  copy to clipboard
map("v", "<leader>y", '"+y')
map("n", "<leader>y", '"+y')
map("v", "<leader>Y", 'gg"+yG')


-- paste from clipboard
map("n", "<leader>p", '"+p')
map("n", "<leader>P", '"+P')

-- select lines
map("n", "<leader>sl", "V")
map("n", "<leader>sh", "V<Home>")
map("n", "<leader>se", "V<End>")
map("n", "<leader>sj", "Vj")
map("n", "<leader>sk", "Vk")

-- move lines
map("n", "<leader>ml", ":m .+1<CR>==")
map("n", "<leader>mh", ":m .-2<CR>==")
map("v", "<leader>ml", ":m '>+1<CR>gv=gv")
map("v", "<leader>mh", ":m '<-2<CR>gv=gv")






map("n", "<C-h>", "<C-w>h")
map("n", "<C-j>", "<C-w>j")
map("n", "<C-k>", "<C-w>k")
map("n", "<C-l>", "<C-w>l")
map("n", "<leader>x", "<C-w>c")

-- nvterm (terminal)
map("n", "<A-t>", ':lua require("nvterm.terminal").toggle "float"<CR>') -- (Normal mode)
map("t", "<A-t>", '<C-\\><C-n><cmd>lua require("nvterm.terminal").toggle "float"<CR>') -- (Terminal mode)
map("n", "<A-h>", ':lua require("nvterm.terminal").toggle "horizontal"<CR>')-- (Normal mode)
map("t", "<A-h>", '<C-\\><C-n><cmd>lua require("nvterm.terminal").toggle "horizontal"<CR>') -- (Terminal mode)
map("n", "<A-H>", ':lua require("nvterm.terminal").toggle "vertical"<CR>') -- (Normal mode)
map("t", "<A-H>", '<C-\\><C-n><cmd>lua require("nvterm.terminal").toggle "vertical"<CR>') -- (Terminal mode)
-- Extras
map("n", "<C-c>", ":%y+<CR>")

