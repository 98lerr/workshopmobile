package jp.co.biglobe.workshopmobile.api.monthlyfee;

import jp.co.biglobe.workshopmobile.domain.エンタメフリーオプション.エンタメフリーオプション;
import jp.co.biglobe.workshopmobile.domain.契約.契約;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@AllArgsConstructor
public class MonthlyFeeApi {

    @RequestMapping(value = "/monthly-fee", method = RequestMethod.GET)
    public Map invoke(
            Request request
    ) {
        Request.PlanForm plan = request.getPlan();
        boolean entame_free = request.isEntame_free();

        契約 contract = 契約.of(plan.getPlan(), new エンタメフリーオプション(entame_free));

        Map<String, Object> res = new HashMap<>();
        res.put("monthly_fee", contract.合算料金を取得する().getValue());
        return res;
    }


}
