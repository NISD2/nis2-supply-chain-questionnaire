import raw from "../data/supplier-questionnaire.json";
import {
  supplierQuestionnaireSchema,
  type SupplierQuestionnaire,
} from "./schema";

export const supplierQuestionnaire: SupplierQuestionnaire =
  supplierQuestionnaireSchema.parse(raw);

export function groupBySection(q: SupplierQuestionnaire) {
  const out = new Map<string, typeof q.fields>();
  for (const field of q.fields) {
    const list = out.get(field.section) ?? [];
    list.push(field);
    out.set(field.section, list);
  }
  return out;
}

export function visibleFields(
  q: SupplierQuestionnaire,
  response: Record<string, unknown>,
) {
  return q.fields.filter((field) => {
    if (!field.visibleWhen) return true;
    return response[field.visibleWhen.field] === field.visibleWhen.equals;
  });
}
