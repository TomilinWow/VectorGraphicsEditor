
class EditorController:
    """
    Класс контроллер
    """
    def __init__(self, model, x, y, w, h, painter):
        self.model = model
        self.model.set_port(x, y, w, h, painter)
        self.active_state = ActiveStateContainer(self.model)

    def change_state(self, new_state):
        self.active_state.change_state(new_state)

    def set_object_type(self, object):
        self.model.set_object_type(object)

    def set_pen_props(self, pen_color, pen_width):
        self.model.set_pen_props(pen_color, pen_width)

    def set_brush_prop(self, brush_prop):
        self.model.set_brush_prop(brush_prop)

    def mouse_clicked(self, x, y):
        self.active_state.mouse_clicked(x, y)

    def mouse_realised(self, x, y):
        self.active_state.mouse_realised(x, y)

    def mouse_move(self, x, y):
        self.active_state.mouse_move(x, y)

    def ctrl_on(self):
        self.active_state.ctrl_on()

    def ctrl_off(self):
        self.active_state.ctrl_off()

    def group(self):
        self.model.group()

    def ungroup(self):
        self.model.ungroup()

    def ungroup_state(self):
        self.active_state.ungroup_state()

    def clear(self):
        self.model.clear()

class ActiveStateContainer:
    """
    Контроль состояний
    """
    def __init__(self, model):
        self.model = model
        self.current_state = None
        self.state = EmptyState(self.model, self)

    def change_state(self, new_state):
        """
        Метод смены состояний
        :param new_state: новое состояние
        """
        self.current_state = new_state

        if self.current_state == "empty":
            self.state = EmptyState(self.model, self)
        elif self.current_state == "create":
            self.state = ObjectCreateState(self.model, self)
        elif self.current_state == "single":
            self.state = SingleSelState(self.model, self)
        elif self.current_state == "multi":
            self.state = MultiSelState(self.model, self)
        elif self.current_state == "drag":
            self.state = DragState(self.model, self)

    def ctrl_on(self):
        self.state.ctrl_on()

    def ctrl_off(self):
        self.state.ctrl_off()

    def ungroup_state(self):
        self.state.ungroup_state()

    def mouse_clicked(self, x, y):
        self.state.mouse_clicked(x, y)

    def mouse_realised(self, x, y):
        self.state.mouse_realised(x, y)

    def mouse_move(self, x, y):
        self.state.mouse_move(x, y)


class State:
    """
    Класс состояния
    """
    def __init__(self, model, active_state):
        self.model = model
        self.active_state = active_state
        self.ctrl_state = False
        self.group_state = False

    def mouse_clicked(self, x, y):
        pass

    def mouse_realised(self, x, y):
        pass

    def mouse_move(self, x, y):
        pass

    def ctrl_on(self):
        self.ctrl_state = True

    def ctrl_off(self):
        self.ctrl_state = False

    def ungroup_state(self):
        self.group_state = True

class ObjectCreateState(State):
    """
    Класс состояния создания
    """
    def __init__(self, model, active_state):
        super().__init__(model, active_state)
        self.model.clear_selection()

    def mouse_clicked(self, x, y):
        self.model.create_object(x, y)
        self.model.try_grab(x, y)
        self.active_state.change_state('drag')

    def mouse_realised(self, x, y):
        pass

    def mouse_move(self, x, y):
        pass

class EmptyState(State):
    """
    Класс пустого состояния
    """
    def __init__(self, model, active_state):
        super().__init__(model, active_state)
        self.model.clear_selection()

    def mouse_clicked(self, x, y):
        if self.model.try_select(x, y):
            self.active_state.change_state("single")
            if self.model.try_grab(x, y):
                self.active_state.change_state("drag")

    def mouse_realised(self, x, y):
        pass

    def mouse_move(self, x, y):
        pass

class DragState(State):
    """
    Класс состояния протяжки
    """
    def __init__(self, model, active_state):
        super().__init__(model, active_state)


    def mouse_realised(self, x, y):
        self.active_state.change_state("single")

    def mouse_move(self, x, y):
        self.model.try_drag_to(x, y)
        self.model.move_state = True


class SingleSelState(State):
    """
    Класс состояния при одном выделении
    """
    def __init__(self, model, active_state):
        super().__init__(model, active_state)


    def mouse_clicked(self, x, y):
        if self.model.try_grab(x, y):
            self.active_state.change_state("drag")

        elif self.model.try_select(x, y):
            if self.ctrl_state:
                self.active_state.change_state("multi")
            else:
                self.model.clear_selection()
                self.model.try_select(x, y)
            self.model.try_grab(x, y)
            self.active_state.change_state("drag")
        else:
            self.active_state.change_state("empty")

    def mouse_realised(self, x, y):
        pass
    def mouse_move(self, x, y):
        pass


class MultiSelState(State):
    """
   Класс состояния при множественном выделении
    """
    def __init__(self, model, active_state):
        super().__init__(model, active_state)

    def mouse_clicked(self, x, y):
        if self.ctrl_state:
            self.model.try_select(x, y)
            self.model.try_grab(x, y)




