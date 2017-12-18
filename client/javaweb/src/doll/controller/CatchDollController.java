package doll.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping(value="/", method = RequestMethod.GET)
public class CatchDollController {

    @RequestMapping(value="catch", method = RequestMethod.GET)
    public String catchDoll(ModelMap model){
        model.addAttribute("msg", "Spring MVC hellow" );
        model.addAttribute("name", "wocao");
        return "CatchDoll";
    }
}
