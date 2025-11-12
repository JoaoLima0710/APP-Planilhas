#!/bin/bash
# Deploy da Edge Function bulk-insert-patients

echo "🚀 Deploying bulk-insert-patients Edge Function..."
supabase functions deploy bulk-insert-patients --project-id pikskrtgivhifxpzrxyb

if [ $? -eq 0 ]; then
  echo "✅ Deploy successful!"
else
  echo "❌ Deploy failed"
  exit 1
fi
