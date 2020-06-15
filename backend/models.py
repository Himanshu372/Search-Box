from django.db import models


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=10, null=False)
    user_id = models.CharField(max_length=12, null=False)
    reviewer_name = models.TextField(default='None')
    prod_helpfulness = models.FloatField(null=False)
    prod_score = models.FloatField(null=False)
    time = models.TextField(null=False)
    summary = models.TextField(null=False)
    text = models.TextField(null=False)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=['product_id'], name='product_id_idx'),
    #         models.Index(fields=['reviewer_name'], name='reviewer_name_idx'),
    #
    #     ]

    @classmethod
    def create(cls, obj_list):
        product_id, user_id, reviewer_name, helpfulness, score, time, summary, text = obj_list
        helpfulness = cls._convert_helpfulness(helpfulness)
        review = cls(product_id=product_id, user_id=user_id, reviewer_name=reviewer_name
                         ,prod_helpfulness=helpfulness, prod_score=score, time=time, summary=summary, text=text)
        return review

    @staticmethod
    def _convert_helpfulness(s):
        s = s.strip()
        if len(s) > 3 or s is None :
            return 0
        num, den = map(int, s.split('/'))
        return round(num / den, 2) if den != 0 else 0.0