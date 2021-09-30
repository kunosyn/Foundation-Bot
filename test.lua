local plr = game.Players.LocalPlayer
local char = plr.Character
local uis = game:GetService("UserInputService")
local tws = game:GetService("TweeningService")

local blast1 = game.Workspace.blast1
local blast2 = game.Workspace.blast2
local blast1_opened = false
local blast2_opened = false
local door_num = 0
local can_open = false
local debounce = false
local door_debounce = false

local door1_open_properties
local door2_open_properties
local door1_closed_properties
local door2_closed_properties

blast1.prox.Touched:Connect(function()
  debounce = true
  can_open = true
  wait(0.1) --> prevents script from recognizing the touch event millions of times

  door1_open_properties = {
    Position = Vector3.new(opened position property)
  }

  door2_open_properties = {
    Position = Vector3.new(opened position property)
  }

  door1_closed_properties = {
    Position = Vector3.new(closed position property)
  }
    door2_closed_properties = {
    Vector3.new(opened position property)
  }

  door_num = 1
  debounce = false
end)

blast1.prox.TouchEnded:Connect(function()
  debounce = true
  can_open = false
  wait(0.1)
  door_num = 0
  debounce = false
end)

blast2.prox.Touched:Connect(function()
  debounce = true
  can_open = true
  wait(0.1) --> prevents script from recognizing the touch event millions of times

  door1_open_properties = {
    Position = Vector3.new(opened position property)
  }

  door2_open_properties = {
    Position = Vector3.new(opened position property)
  }

  door1_closed_properties = {
    Position = Vector3.new(closed position property)
  }
  door2_closed_properties = {
    Vector3.new(opened position property)
  }

  door_num = 2
  debounce = false
end)

blast2.prox.TouchEnded:Connect(function()
  debounce = true
  can_open = false
  wait(0.1)
  door_num = 0
  debounce = false
end)

local door_opening = TweenInfo.new(
  2.55,
  Enum.EasingStyle.Cubic,
  Enum.EasingDirection.Out,
  false,
  0,
  false
)

local door_closing = TweenInfo.new(
  2.55,
  Enum.EasingStyle.Cubic,
  Enum.EasingDirection.In,
  false,
  0,
  false
)

uis.InputBegan:Connect(function(key)
  if key.KeyCode == Enum.KeyCode.E then 
    if can_open == true then
      if door_num == 1 then
        if blast1_opened == false and door_debounce == false then
          door_debounce == true
          door1_tween = tws.new(blast1.door1, door_opening, door1_open_properties)
          door2_tween = tws.new(blast1.door2, door_opening, door2_open_properties)
          door1_tween:Play()
          door2_tween:Play()
          wait(2)
          blast1_opened = true
          door_debounce == true
        elseif blast1_opened == true and door_debounce == false then
          door_debounce == true
          door1_tween = tws.new(blast1.door1, door_closing, door1_closed_properties)
          door2_tween = tws.new(blast1.door2, door_closing, door2_closed_properties)
          door1_tween:Play()
          door2_tween:Play()
          wait(2)
          blast1_opened = false
          door_debounce == true
        end
      elseif door_num == 2 then
        if blast2_opened == false and door_debounce == false then
          door_debounce == true
          door1_tween = tws.new(blast2.door1, door_opening, door1_open_properties)
          door2_tween = tws.new(blast2.door2, door_opening, door2_open_properties)
          door1_tween:Play()
          door2_tween:Play()
          wait(2)
          blast2_opened = true
          door_debounce == true
        elseif blast2_opened == true and door_debounce == false then
          door_debounce == true
          door1_tween = tws.new(blast2.door1, door_closing, door1_closed_properties)
          door2_tween = tws.new(blast2.door2, door_closing, door2_closed_properties)
          door1_tween:Play()
          door2_tween:Play()
          wait(2)
          blast2_opened = false
          door_debounce == true
        end
      end
    end
  end
end)